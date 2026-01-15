pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }
        
        stage('Setup Environment') {
            steps {
                echo 'Setting up test environment...'
                sh '''
                    python3 --version
                    pip3 --version
                '''
            }
        }
        
        stage('Run Calculator Tests') {
            steps {
                echo 'Running Calculator Tests...'
                sh 'python3 test_calculator.py'
            }
        }
        
        stage('Run String Operation Tests') {
            steps {
                echo 'Running String Operation Tests...'
                sh 'python3 test_string_operations.py'
            }
        }
        
        stage('Test Summary') {
            steps {
                echo 'All tests completed successfully!'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
        always {
            echo 'Cleaning up workspace...'
            cleanWs()
        }
    }
}
