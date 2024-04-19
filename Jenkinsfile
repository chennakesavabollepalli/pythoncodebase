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
             echo "${GIT_TAG}"
          """
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
