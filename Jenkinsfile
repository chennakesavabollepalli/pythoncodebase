pipeline {
  agent any 
  environment { 
  DOCKER_IMAGE = 'chenna/pythoncodebase:01'
  DOCKER_CREDENTIALS = 'docker-hub-credentials'
  }
stages { 
stage {
  steps {
    script {
      docker.build(env.DOCKER_IMAGE)
    }
  }
}
stage {
  steps { 
  script { 
    docker.withRegistry('https://index.docker.io/v1/', env.DOCKER_REGISTRY_CREDENTIALS) {
    docker.image(env.DOCKER_IMAGE).push('latest')    
  }
  }
}
}
post { 
  success {
    echo "Success - Docker image build and pushed to Docker hub!"
    
  }
  failure { 
    echo "Failed to build and pushed to Docker hUb!"
  }
}
    
}
}
