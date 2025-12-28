pipeline {
    agent any

    environment {
        IMAGE_NAME = "wisdom-app"
    }

    stages {
        // שלב הבנייה - רץ תמיד
        stage('Build') {
            steps {
                echo "Building Docker Image..."
                sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .'
            }
        }

        // שלב הבדיקות - רץ תמיד
        stage('Test') {
            steps {
                echo "Running Unit Tests..."
                sh 'docker run --rm ${IMAGE_NAME}:${BUILD_NUMBER} pytest'
            }
        }

        // שלב ההפצה - רץ רק ב-Main!
        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                echo "Deploying to Production Server..."
                echo "This step only runs on MAIN branch!"
                // בשלבים הבאים נכניס פה את הלוגיקה האמיתית
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'docker rmi ${IMAGE_NAME}:${BUILD_NUMBER} || true'
        }
    }
}
