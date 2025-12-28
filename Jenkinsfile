pipeline {
    agent any

    environment {
        // חובה: החלף בשם המשתמש שלך ב-DockerHub
        DOCKER_USER = "ofekpensso" 
        
        // שם האימג' חייב להיות בפורמט: user/repo
        IMAGE_NAME = "${DOCKER_USER}/wisdom-app"
        
        // מזהה הסוד שיצרנו בג'נקינס
        DOCKER_CRED_ID = "docker-hub-credentials"
    }

    stages {
        stage('Build') {
            steps {
                echo "Building..."
                // בנייה עם תיוג מלא
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
                echo "Pushing to Docker Hub..."
                // שימוש בפרטי ההתחברות בצורה מאובטחת
                withCredentials([usernamePassword(credentialsId: DOCKER_CRED_ID, usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    // 1. התחברות
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                    
                    // 2. דחיפת הגרסה הספציפית (למשל v15) - לגיבוי והיסטוריה
                    sh 'docker push ${IMAGE_NAME}:${BUILD_NUMBER}'
                    
                    // 3. יצירת תיוג "latest" ודחיפה שלו - לשימוש קל
                    sh 'docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest'
                    sh 'docker push ${IMAGE_NAME}:latest'
                    
                    // 4. התנתקות (אבטחה)
                    sh 'docker logout'
                }
            }
        }

        stage('Deploy to Production') {
            when { branch 'main' }
            steps {
                echo "Deploying..."
                // בקרוב...
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // מחיקת האימג'ים מהשרת המקומי (הם כבר בטוחים בענן)
            sh 'docker rmi ${IMAGE_NAME}:${BUILD_NUMBER} || true'
            sh 'docker rmi ${IMAGE_NAME}:latest || true'
        }
    }
}
