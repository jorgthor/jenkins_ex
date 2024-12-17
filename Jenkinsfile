pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "jorgthor/jenkins_ex"
        DOCKER_CREDENTIALS = "docker-hub-credentials" // Jenkins credentials ID
        //GITHUB_REPO = "https://github.com/your-username/your-repo.git"
        DOCKER_TAG = "latest"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo "Pulling code from GitHub..."
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing dependencies..."
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install unittest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running tests..."
                sh '''
                source venv/bin/activate
                unittest tests/test_main.py
                unittest tests/test_functions.py
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
            }
        }

        stage('Push Docker Image to Hub') {
            steps {
                echo "Pushing Docker image to Docker Hub..."
                withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIALS}", usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                    echo "*** Logging into Docker Hub ***"
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    echo "*** Pushing Docker Image ***"
                    docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                    '''
                }
            }
        }

        stage('Clean Up') {
            steps {
                echo "Cleaning up local Docker images and workspace..."
                sh '''
                docker rmi ${DOCKER_IMAGE}:${DOCKER_TAG} || true
                rm -rf venv
                '''
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check the logs for errors."
        }
        always {
            echo "Pipeline finished."
        }
    }
}