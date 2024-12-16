pipeline {
    agent { dockerfile true }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python3 -m py_compile main.py functions.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'python3 -m unittest discover'
            }
        }
    }
}