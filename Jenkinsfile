pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python -m py_compile main.py functions.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'python3 -m unittest discover -s tests -p "*_test.py" --junit-xml test-reports/results.xml'
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                }
            }
        }
    }
}