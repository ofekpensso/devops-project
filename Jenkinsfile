pipeline {
    agent any

    environment {
        IMAGE_NAME = "wisdom-app"
    }

    stages {
        stage('Build') {
            steps {
                echo "Building Docker Image..."
                sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .'
            }
        }

        stage('Test') {
            steps {
                echo "Running Unit Tests..."
                // הרצת קונטיינר זמני שמריץ את הפקודה pytest ונסגר מיד
                sh 'docker run --rm ${IMAGE_NAME}:${BUILD_NUMBER} pytest'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // מחיקת האימג' בסוף הריצה (בין אם הצליח ובין אם נכשל)
            sh 'docker rmi ${IMAGE_NAME}:${BUILD_NUMBER} || true'
        }
    }
}
