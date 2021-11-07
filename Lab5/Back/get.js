const AWS = require('aws-sdk');
const ddb = new AWS.DynamoDB.DocumentClient({region: 'us-east-2'});
exports.handler = async (event) => {
    let values;
    try{
        values = await ddb.scan({
            TableName: 'Binnacle'
        }).promise();

        
        return { 
            StatusCode: 200, StatusMessage: 'Data Read Successfully','Body':values["Items"] 
            
        }; 
    }catch(err){
        return {
            StatusCode: 400,
            StatusMessage: "Wrong table provided"
        };
    }
};
