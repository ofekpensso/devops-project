pipeline {
    agent any

    environment {
        // הגדרת שם האפליקציה כמשתנה סביבה לשימוש חוזר
        IMAGE_NAME = "wisdom-app"
    }

    stages {
        stage('Build') {
            steps {
                echo "Building Docker Image version: ${env.BUILD_NUMBER}"
                // בניית האימג' ותיוג שלו עם מספר הריצה הנוכחי
                sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .'
            }
        }
    }

    // חלק קריטי לשרתים קטנים כמו שלנו!
    post {
        success {
            echo 'Build successful!'
        }
        always {
            // ניקוי: מחיקת האימג' שנוצר כדי לא לסתום את הדיסק של השרת
            echo 'Cleaning up workspace and images...'
            sh 'docker rmi ${IMAGE_NAME}:${BUILD_NUMBER} || true'
        }
    }
}
