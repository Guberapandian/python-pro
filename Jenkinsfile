node {
    stage('Git Checkout') {
        git branch: 'main', url: 'https://github.com/Guberapandian/python-pro.git'
    }

    stage('Build Docker Image') {
        sh 'docker build -t guberapandian/python-pro:latest .'
    }

    stage('Docker Push') {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'dockerUsername', passwordVariable: 'dockerPassword')]) {
            sh '''
                echo $dockerPassword | docker login -u $dockerUsername --password-stdin
                docker push guberapandian/python-pro:latest
            '''
        }
    }

    stage('Docker Deployment') {
        sh '''
            docker stop python || true
            docker rm python || true
            docker run -d -p 8090:8000 --name python guberapandian/python-pro:latest
        '''
    }
}
