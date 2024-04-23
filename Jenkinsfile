pipeline {
  agent any 
  environment { 
    // GIT_TAG = "${env.TAG_NAME}"
    git_branch = env.BRANCH_NAME
  }
  stages { 
    stage('Checkout') {
      steps {
        checkout scm: [
          $class: 'GitSCM',
          branches: [[name: "refs/heads/${git_branch}"]],
          userRemoteConfigs: [[url: 'https://github.com/chennakesavabollepalli/pythoncodebase.git']]
        ]

        
      }
    }
    stage('POC') {
      steps {
        script {
          // def tagName = env.TAG_NAME
          if (env.TAG_NAME) {
              println "Prent Git tag:" env.TAG_NAME
          } else {
              println "This build was not having by a git tag"
          }
          



        
        }
      }
    }
    stage ('poc new') {
      steps {
        script {
           def Git_Tag = sh(script: 'git describe --tags --abbrev=0', returnStdout: true).trim()
           echo "git tag is ${Git_Tag}"
           if (Git_Tag) {
              println "Prent Git tag: ${Git_Tag}"
           } else {
              println "This build was not having by a git tag"
           }
        }
      }
    }
  }


}
