def qa_stage_run=false


pipeline {

    agent any
    environment {
        SNYK_TOKEN = credentials('snyk-api-token')
        ZAP_DOCKER_IMAGE = 'owasp/zap2docker-stable'
        scannerHome = tool 'SonarQube'
    }
    stages {
        stage ('checkout') {
                    steps {
                        sh 'mkdir -p build'
                        dir("build")
                        {
                            git branch: "main",
                            credentialsId: "raj-epam",
                            url: 'https://github.com/raj-epam/appdeploydemo-fe.git'
                        }
                    }
                }

        //     }
        // }
    stage ("Scan Code") {
        steps {
            dir("build") {
                sh 'pip install -r requirements.txt '
                //def scannerHome = tool 'sonarqube'
                //env.PATH = "${scannerHome}/bin:${env.PATH}"
            }
            dir("build/app") {
                withSonarQubeEnv(installationName: 'sonarqube') {
                    sh '${scannerHome}/bin/sonar-scanner'
            }
        }
    }
}
    stage ("Test Code") {
        steps {
            dir("build") {
                sh 'pip install -r requirements.txt '
                //def scannerHome = tool 'sonarqube'
                //env.PATH = "${scannerHome}/bin:${env.PATH}"
            }
            dir("build/test") {
                sh 'python3 -m venv venv'
                sh 'python3 -m unittest discover tests'
            }
        }
    }    
    
    

    // stage ('Build') {
    //         steps {
    //             dir("build")
    //             {
    //                 sh 'docker build -t dhlawowacr.azurecr.io/pywebapp:${BUILD_NUMBER} .'
    //             }
    //         }
    //     }
    // stage('SYNK Scan') {
    //     steps {
    //         script{
    //             dir("build")
    //                 {   
    //                     echo "Current workspace is ${WORKSPACE}"
    //                     sh 'rm -f vulnerabilities.json'
    //                     echo "Starting Scan"
    //                     def scanExitCode = sh(script: 'snyk container test dhlawowacr.azurecr.io/pywebapp:${BUILD_NUMBER}  --file=./Dockerfile --json-file-output=vulnerabilities.json --org=raj-epam --project-name=python_demo-FE', returnStatus: true)
    //                     def display = sh(script: 'snyk container monitor dhlawowacr.azurecr.io/pywebapp:${BUILD_NUMBER}  --file=./Dockerfile --org=raj-epam --project-name=python_demo-FE --project-environment=frontend', returnStatus: true)
    //                     archiveArtifacts 'vulnerabilities.json'
                        
    //                     echo "error code = ${scanExitCode}"
    //                 }
    //             }
    //         }
    //     }


    //     stage('Run DAST Scan') {
    //         steps {
    //             script {
                    
    //                 sh 'docker stop my-python-app || true'
    //                 sh 'docker rm -f my-python-app || true'
    //                 // Run your Python application in a Docker container
    //                 def dockerRunCmd = """docker run -d --name my-python-app -p 80:5000 dhlawowacr.azurecr.io/pywebapp:${BUILD_NUMBER}"""
    //                 sh dockerRunCmd
    //                 // Run ZAP DAST scan against the running application
    //                 //def zapScanCmd = """"""
    //                 def SAST_SCAN= sh(script:"docker run --rm -v ${WORKSPACE}:/zap/wrk/:rw --user root owasp/zap2docker-stable zap-baseline.py  -t http://\$(ip -f inet -o addr show docker0 | awk '{print \$4}' | cut -d '/' -f 1):80 -g gen.conf -r report.html", returnStatus: true)
    //                 archiveArtifacts 'report.html'
    //                 echo "error code = ${SAST_SCAN}"
    //                 // Stop and remove the running Python application container
    //                 sh 'docker stop my-python-app && docker rm my-python-app'
    //             }
    //         }
    //     }



    //     stage('Push Image') {//Manifest Deploy for Dev Env Values
    //         steps {
    //         dir("build")
    //         { withCredentials([string(credentialsId: 'svc_principal', variable: 'PASSWORD')]) {
    //                     sh "az login --service-principal -u 01c88a92-5b91-4664-a88a-6b39f649ce24 -p $PASSWORD  --tenant b41b72d0-4e9f-4c26-8a69-f949f367c91d"
    //             }
    //             sh "az account set --subscription 40d692fa-1896-4563-9f1d-95ae2fa15c38"
    //             sh "az acr login --name dhlawowacr"
    //             sh 'docker push dhlawowacr.azurecr.io/pywebapp:${BUILD_NUMBER}'       
    //             sh 'docker image rm dhlawowacr.azurecr.io/pywebapp:${BUILD_NUMBER}'                    
    //         }
    //         cleanWs()
    //         }
    //     }

        // stage ('Push') {
        //     steps {
        //         dir("build")
        //         {
        //             
        //         }
        //     }
    // }
    }
        post {
            // Clean after build
            always {
                cleanWs(cleanWhenNotBuilt: false,
                        deleteDirs: true,
                        disableDeferredWipeout: true,
                        notFailBuild: true,
                        patterns: [[pattern: '.gitignore', type: 'INCLUDE'],
                                [pattern: '.propsfile', type: 'EXCLUDE']])
            }
    }


}