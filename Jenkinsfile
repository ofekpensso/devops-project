pipeline {
    agent any

    stages {
        stage('Init') {
            steps {
                echo 'Starting the DevOps Wisdom Pipeline...'
                // בדיקה שג׳נקינס מצליח לגשת לדוקר
                sh 'docker --version' 
            }
        }
        
        stage('Test SCM') {
            steps {
                // בדיקה שג׳נקינס רואה את הקבצים שלנו
                sh 'ls -la'
            }
        }
    }
}
