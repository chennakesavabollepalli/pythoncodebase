pipeline {
  agent any 
  environment { 
    GIT_TAG = "${env.TAG_NAME}"
  }
  stages { 
    stage {
      steps {
        script {
          sh """
             echo ${GIT_TAG}
          """
        }
      }
    }
    // stage {
    //   steps { 
    //     script { 
    //       docker.withRegistry('https://index.docker.io/v1/', env.DOCKER_REGISTRY_CREDENTIALS) 
    //       docker.image(env.DOCKER_IMAGE).push('latest')    
    //     }
    //   }
    // }
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
