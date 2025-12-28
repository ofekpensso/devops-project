pipeline {
    agent any

    environment {
        // החלף בשם המשתמש שלך
        DOCKER_USER = "ofekpenso" 
        IMAGE_NAME = "${DOCKER_USER}/wisdom-app"
        DOCKER_CRED_ID = "docker-hub-credentials"
        
        // שם קבוע לקונטיינר שרץ בייצור (כדי שנוכל למצוא ולמחוק אותו)
        CONTAINER_NAME = "wisdom-app-prod"
    }

    stages {
        stage('Build') {
            steps {
                echo "Building..."
                sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .'
            }
        }

        stage('Test') {
            steps {
                echo "Testing..."
                sh 'docker run --rm ${IMAGE_NAME}:${BUILD_NUMBER} pytest'
            }
        }

        stage('Push to Docker Hub') {
            when { branch 'main' }
            steps {
                echo "Pushing..."
                withCredentials([usernamePassword(credentialsId: DOCKER_CRED_ID, usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                    sh 'docker push ${IMAGE_NAME}:${BUILD_NUMBER}'
                    sh 'docker logout'
                }
            }
        }

        stage('Deploy to Production') {
            when { branch 'main' }
            steps {
                echo "Deploying version ${BUILD_NUMBER} to Production..."
                script {
                    // 1. עצירת הקונטיינר הישן (ה- '|| true' מונע שגיאה אם הוא לא קיים)
                    sh "docker stop ${CONTAINER_NAME} || true"
                    
                    // 2. מחיקת הקונטיינר הישן
                    sh "docker rm ${CONTAINER_NAME} || true"
                    
                    // 3. הרצת הקונטיינר החדש
                    // אנחנו משתמשים בדיוק בגרסה שבנינו הרגע (${BUILD_NUMBER})
                    sh "docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}:${BUILD_NUMBER}"
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            // מחיקת האימג' שנבנה לטובת ה-Build כדי לחסוך מקום
            // (הפקודה run בשלב ה-Deploy תמשוך אותו מחדש או תשתמש ב-cache אם נשאר)
            sh 'docker rmi ${IMAGE_NAME}:${BUILD_NUMBER} || true'
        }
    }
}
