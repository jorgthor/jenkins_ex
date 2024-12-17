pipeline {
    agent { dockerfile true }
    def dockerAccount = 'jorgthor'
    def appName = jenkins_ex
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code..'
                checkout scm
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'python3 -m unittest tests/test_main.py tests/test_functions.py'
            }
        }
        stage('Build') {
            steps {
                echo 'Building..'
                app = docker.build("${dockerAccount}/${appName}")
            }
        }
        stage('Push to DockerHub') {
            steps {
                echo 'Pushing to Dockerhub....'
                docker.withRegistry('https://index.docker.io/v1/', $dockerAccount) {
                    app.push("${env.BUILD_NUMBER}")
                    app.push("latest")
                }
            }
        }
        stage('Cleanup') {
            steps {
                echo 'Cleaning up..'
                script {
                    app.remove()
                }
            }
        }
    }
}