"""-----------------------------------------------------------------------------------------------------
                          Wine classifier-
                    (Student name - Vaishali Jorwekar)
--------------------------------------------------------------------------------------------------------
Problem statement: Dataset contains information about Wine type based on some features
                   Multi-class classification of Wine Type using Decision Tree and  Random Forest
--------------------------------------------------------------------------------------------------------"""
#####################################################################################################
# Required Python Packages
#####################################################################################################
import pandas as pd
import os,argparse
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib
from sklearn.metrics import (accuracy_score,confusion_matrix,classification_report,
                             ConfusionMatrixDisplay)
#####################################################################################################
# Constants and file names
#####################################################################################################
BORDER="-"*65
DATASET_FILENAME="WinePredictor.csv"
ARTIFACT_DIR="artifact_WineClassification"
RANDOM_STATE=42
TEST_SIZE=0.2
TARGET_COLUMN="Class"
"""Classification model list"""
CLF_MODELS=  {"Decision Tree Classifier":DecisionTreeClassifier(),
              "Random Forest Classifier":RandomForestClassifier()}

#####################################################################################################
###########################################################################################
#   Function        :   ensure_dir
#   Input Params    :   path(str)-directory path
#   Output Params   :   None
#   Description     :   Creates a directory if it does not exists
#   Author          :   Vaishali M Jorwekar
#   Date            :   1 Oct 2025
############################################################################################
def ensure_dir(path:str):
    os.makedirs(path,exist_ok=True)
###########################################################################################
#   Function        :   parse_args
#   Input Params    :   None
#   Output Params   :   Parsed CLI arguments
#   Description     :   Defines command line arguments for training ,interference baselines
#   Author          :   Vaishali M Jorwekar
#   Date            :   21 Oct 2025
############################################################################################
def parse_args():
    p=argparse.ArgumentParser(description="Wine Classification Case Study")
    p.add_argument("--train",action="store_true",
                   help="Train Using 'Decision Tree & Random Forest' and Save Artifacts")
    p.add_argument("--test",action="store_true",help="Test the model using saved model")
    p.add_argument("--samples",type=int,default=10,help="Number of samples for testing ")
    return p.parse_args() 
###########################################################################################
#   Function        :   displayCoRelationMatrix
#   Input Params    :   dFrame(data frame)
#   Output Params   :   -
#   Description     :   Displays co-relation matrix
#   Author          :   Vaishali M Jorwekar
#   Date            :   1 Oct 2025
############################################################################################
def displayCoRelationMatrix(dFrame):
    print(BORDER)
    ensure_dir(ARTIFACT_DIR)
    plt.figure(figsize=(10,6))
    sns.heatmap(dFrame.corr(),annot=True,cmap="coolwarm")
    plt.title("Feature co-relation heatmap")
    #plt.show()
    plt.savefig(os.path.join(ARTIFACT_DIR,"CoRelationMatrix.png")) 
###########################################################################################
#   Function        :   preProcessData
#   Input Params    :   None
#   Output Params   :   df(Data Frame)
#   Description     :   Load CSV data and pre-process data
#   Author          :   Vaishali M Jorwekar
#   Date            :   1 Oct 2025
############################################################################################
def preProcessData():
    #Load data from CSV file
    df=readCSVFile(csvFileName=DATASET_FILENAME)
    #Clean data set
    df=cleanDataSet(df)
    #Print co-relation matrix
    displayCoRelationMatrix(df)
    return df
###########################################################################################
#   Function        :   readCSVFile
#   Input Params    :   dataSetFile
#   Output Params   :   Pandas data drame
#   Description     :   Load CSV data and return pandas data drame
#   Author          :   Vaishali M Jorwekar
#   Date            :   1 Oct 2025
############################################################################################
def readCSVFile(csvFileName=DATASET_FILENAME)->pd.DataFrame:
    dFrame=pd.read_csv(csvFileName)
    print(BORDER)
    print(f"Data loaded successfully from file '{csvFileName}'")
    print(BORDER)
    print(f"File Data:\n{BORDER}\n{dFrame.describe()}")
    print(BORDER)
    return dFrame
###########################################################################################
#   Function        :   cleanDataSet
#   Input Params    :   dFrame(data frame)
#   Output Params   :   Updated data frame 
#   Description     :   Cleans data set by removing unwanted columns
#   Author          :   Vaishali M Jorwekar
#   Date            :   1 Oct 2025
############################################################################################
def cleanDataSet(dFrame)->pd.DataFrame:
    print(BORDER)
    print("Cleaning Data set....")
    print(BORDER)
    print("Dimensions of data set before cleaning is :",dFrame.shape)
    #Remove unwanted data
    dFrame.dropna(inplace=True)
    print(BORDER)
    print("Wine class prediction data set after cleaning")
    print(dFrame.head())
    return dFrame
###########################################################################################
#   Function        :   findFeaturesAndTarget
#   Input Params    :   dFrame(data frame)
#   Output Params   :   independent and dependent variables
#   Description     :   This method spilts data set into features and target
#   Author          :   Vaishali M Jorwekar
#   Date            :   1 Oct 2025
############################################################################################
def findFeaturesAndTarget(dFrame):
    xFeatures=dFrame.drop(columns=[TARGET_COLUMN])
    yTarget=dFrame[TARGET_COLUMN]
    print(BORDER)    
    return xFeatures,yTarget
###########################################################################################
#   Function        :   spliDataSet
#   Input Params    :   dFrame(data frame)
#   Output Params   :   independent and dependent variables
#   Description     :   This method spilts data set into features and labels
#   Author          :   Vaishali M Jorwekar
#   Date            :   1 Oct 2025
############################################################################################
def spliDataSet(dFrame):
    xFeatures,yTarget=findFeaturesAndTarget(dFrame)
   
    x_Train,x_Test,y_Train,y_Test=train_test_split(xFeatures,
                                                   yTarget,
                                                   test_size=TEST_SIZE,
                                                   random_state=RANDOM_STATE)
    return x_Train,x_Test,y_Train,y_Test
#####################################################################################################
#   Function name    :  build_Pipeline
#   Input Params     :  clf_Name: model name
#   Output           :  Return pipeline object
#   Description      :  Build a pipeline
#   Author          :   Vaishali M Jorwekar
#   Date            :   1 Oct 2025
#####################################################################################################
def build_Pipeline(clf_Name):
    pipe=Pipeline(steps=[
         ("scalar",StandardScaler()),
         ("clf",clf_Name),
    ])
    return pipe 
#####################################################################################################
#   Function name    :  trainPipeline
#   Input Params     :  pipeline,xTrain,yTrain data set
#   Output           :  Return pipeline object
#   Description      :  Train a pipeline
#   Author          :   Vaishali M Jorwekar
#   Date            :   1 Oct 2025
#####################################################################################################
def trainPipeline(pipeline,xTrain,yTrain):
    pipeline.fit(xTrain,yTrain)
    return pipeline     
#####################################################################################################
#   Function name    :  testModelAndAccuracyCalculation
#   Input Params     :  pipeline,xTrain,yTrain data set
#   Output           :  Return pipeline object
#   Description      :  Train a pipeline
#   Author          :   Vaishali M Jorwekar
#   Date            :   1 Oct 2025
#####################################################################################################
def testModelAndAccuracyCalculation(model,x_Test,y_Test):
    """Predict the test results"""
    model_Predicted=model.predict(x_Test)
    """Accuracy calculations"""
    model_Accuracy=accuracy_score(y_Test,model_Predicted)
    """Calculate confusion Matrix """
    model_ConfusionMatrix=confusion_matrix(y_Test,model_Predicted)
    """Model classification report"""
    model_Classification_Report=classification_report(y_Test,model_Predicted)
    return model_Accuracy,model_ConfusionMatrix,model_Classification_Report
###########################################################################################
#   Function        :   plotAndSaveAccuracyScore
#   Input Params    :   Dictionary holding all details
#   Output Params   :   -
#   Description     :   Plot and saves accuracy score
#   Author          :   Vaishali M Jorwekar
#   Date            :   1 oct 2025
############################################################################################    
def plotAndSaveAccuracyScore(algorithmDetails):
    ensure_dir(ARTIFACT_DIR)
    x=algorithmDetails['Algorithm Name']
    y=algorithmDetails['Accuracy Score']
    plt.figure(figsize=(8,7))
    plt.bar(x,y,width=0.4)
    plt.title('Accuracy of algorithms')
    plt.xlabel('Algorithm')
    plt.ylabel('Accuracy')
    plt.yticks(y)
    plt.grid(True)
    #plt.show()
    outDir=os.path.join(ARTIFACT_DIR,"AccuracyPlot.png")
    plt.savefig(outDir)
    plt.close()
    print(f"Saved Accuracy Plot :{outDir}")
###########################################################################################
#   Function        :   plotConfusionMatrix
#   Input Params    :   Dictionary holding all details
#   Output Params   :   -
#   Description     :   Saves confusion matrix
#   Author          :   Vaishali M Jorwekar
#   Date            :   1 Oct 2025
############################################################################################    
def plotConfusionMatrix(algorithmDetails):
    ensure_dir(ARTIFACT_DIR)
    """Create the figure and subplots
    As we used 2 algorithms use Subplots to plot 2 confusion matrix"""
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 5)) 
    for cnt in range(len(algorithmDetails["Confusion Matrix"])):
        
        confuMatrix = ConfusionMatrixDisplay(confusion_matrix=algorithmDetails["Confusion Matrix"][cnt])
        confuMatrix.plot(ax=axes[cnt])
        axes[cnt].set_title(algorithmDetails["Algorithm Name"][cnt])
    plt.tight_layout()
    #plt.show()
    plt.savefig(os.path.join(ARTIFACT_DIR,"ConfusionMatrix.png"))
    plt.close()
###########################################################################################
#   Function        :   save_classification_report
#   Input Params    :   algorithmDetails(Dictionary holding all details)
#   Output Params   :   Saves classification report
#   Description     :   prints and saves classification report with precision,recall,F1 score
#   Author          :   Vaishali M Jorwekar
#   Date            :   1 Oct 2025
##########################################################################################
def save_classification_report(algorithmDetails):
    out_dir=ARTIFACT_DIR
    ensure_dir(out_dir)
    reportData=""
    for cnt in range(len(algorithmDetails["Classification Report"])):
        reportData=f"{reportData}\t{algorithmDetails["Algorithm Name"][cnt]}\n{BORDER}"
        clsReport=algorithmDetails["Classification Report"][cnt]
        reportData=f"{reportData}\n{clsReport}{BORDER}\n\n"
    with open (os.path.join(out_dir,"classification_report.txt"),"w") as f:
        f.write(reportData)  
#####################################################################################################
#   Function name    :  saveTrainedModel
#   Input Params     :  model,modelName
#   Output           :  -
#   Description      :  Save the trained model
#   Author          :   Vaishali M Jorwekar
#   Date            :   1 Oct 2025
#####################################################################################################
def saveTrainedModel(model,modelName):
    path=os.path.join(ARTIFACT_DIR,modelName+".joblib")
    joblib.dump(model,path)
    print(f"Model saved to path :{path}")            
###########################################################################################
#   Function        :   train_and_evaluate
#   Input Params    :   None
#   Output Params   :   Parsed CLI arguments
#   Description     :   Defines command line arguments for training,testing
#   Author          :   Vaishali M Jorwekar
#   Date            :   1 Oct 2025
############################################################################################
def train_and_evaluate():
    #Load CSV and pre-process data
    df=preProcessData()
    #Split data set  
    x_Train,x_Test,y_Train,y_Test=spliDataSet(df)

    #Decision Tree Classifier
    dTree=build_Pipeline(DecisionTreeClassifier(max_depth=10))
     #Train Model
    dTree=trainPipeline(dTree,x_Train,y_Train)
    dTreeAccuracy,dTConfusionMatrix,dTClassificationReport\
                            =testModelAndAccuracyCalculation(dTree,x_Test,y_Test)
    
     #Random Forest 
    rForest=build_Pipeline(RandomForestClassifier(max_depth=10))
     #Train Model
    rForest=trainPipeline(rForest,x_Train,y_Train)
    rForestAccuracy,rForestConfusionMatrix,rForestClassificationReport\
                            =testModelAndAccuracyCalculation(rForest,x_Test,y_Test)
    

    algorithmDetails={"Algorithm Name":["Decision Tree Classifier","Random Forest Classifier"],
                      "Accuracy Score":[dTreeAccuracy*100,rForestAccuracy*100],
                      "Confusion Matrix":[dTConfusionMatrix,rForestConfusionMatrix],
                      "Classification Report":[dTClassificationReport,rForestClassificationReport]}
    #Plot and save accuracy plot and accuracy score
    plotAndSaveAccuracyScore(algorithmDetails)
    #Plot confusion matrix
    plotConfusionMatrix(algorithmDetails)
    #Save classification Report
    save_classification_report(algorithmDetails)
    #Save Trained models
    saveTrainedModel(dTree,algorithmDetails["Algorithm Name"][0])
    saveTrainedModel(rForest,algorithmDetails["Algorithm Name"][1])
#####################################################################################################
#   Function name    :  loadTrainedModel
#   Input Params     :  path = MODEL_PATH
#   Output           :  model
#   Description      :  Load the trained model
#   Author          :   Vaishali M Jorwekar
#   Date            :   1 Oct 2025
#####################################################################################################
def loadTrainedModel(modelName):  
    path=modelName+".joblib"
    path=os.path.join(ARTIFACT_DIR,path)
    model = joblib.load(path)
    print(f"Model loaded from the path :{path}")
    return model  
#####################################################################################################
#   Function name    :  testTrainedModel
#   Input Params     :  path = MODEL_PATH,n_samples
#   Output           :  model
#   Description      :  Test the trained model
#   Author          :   Vaishali M Jorwekar
#   Date            :   1 Oct 2025
#####################################################################################################
def testTrainedModel(model,sampleTestData): 
     predictedResult=model.predict(sampleTestData.drop(columns=[TARGET_COLUMN]))
     predictionAccuracy=accuracy_score(sampleTestData[TARGET_COLUMN],predictedResult)
     return predictionAccuracy,predictedResult    
###########################################################################################
#   Function        :   test_models
#   Input Params    :   n_samples(Number of samples)
#   Output Params   :   -
#   Description     :   Test loaded model
#   Author          :   Vaishali M Jorwekar
#   Date            :   1 Oct 2025
############################################################################################    
def test_models(n_samples):
    df=preProcessData()
    sampleTestData =df.sample(n=n_samples)
    #Copy test data
    copyTestData=sampleTestData.copy()
    print(BORDER)
    print(f"Selected sample data for testing are \n: {sampleTestData}")
    print(BORDER)

    """Loading saved model and sample tetsing"""
    testResult=""
    for clf_Name,clfModel in CLF_MODELS.items():  
        print(f"Sample testing Using : {clf_Name}")  
        # Load the model and test samples
        trainedModel=loadTrainedModel(clf_Name)
        # Test Model on a random sample from data set
        predictionAccuracy,predictedResult=testTrainedModel(trainedModel,sampleTestData)
        copyTestData["Predicted Result"]=predictedResult
        testResult=f"\n{testResult}{clf_Name}\n{BORDER}\n{copyTestData}\n\
            \nTesting Accuracy:{predictionAccuracy*100}\n{BORDER}\n"
    outDir=os.path.join(ARTIFACT_DIR,"PredictedResult.txt")
    with open(outDir,"w") as f:
         f.write(str(testResult))
#####################################################################################################
#   Function Name    :  main function 
#   Description      :  main function,manages calls to other functions
#   Input Params     :  -   
#   Output Params    :  -
#   Author          :   Vaishali M Jorwekar
#   Date            :   1 Oct 2025
#####################################################################################################
def main():
    ensure_dir(ARTIFACT_DIR)
    args=parse_args()
    did_anything=False
    #Train Model
    if args.train:
        train_and_evaluate()
        did_anything=True
    #Model testing    
    if args.test:
        test_models(n_samples=args.samples)
        did_anything=True    
    if not did_anything:
        print(
            "Nothing to do .Try one of the :\n"
            "python3 WinePredictor.py --train\n"
            "python3 WinePredictor.py --test\n"
        )      
#####################################################################################################
#     Starter
#####################################################################################################
if __name__=="__main__":
    main()
