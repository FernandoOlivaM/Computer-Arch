const AWS = require('aws-sdk');
const ddb = new AWS.DynamoDB.DocumentClient({region: 'us-east-2'});
exports.handler = async (event) => {
    let values;
    try{
        values = await ddb.scan({
            TableName: 'Binnacle'
        }).promise();
        
        let lastInserted = values["Items"][0];
        for (var i = 0; i < values["Items"].length; i++) {
            if(values["Items"][i]["TimeStampUpdated"] > lastInserted["TimeStampUpdated"]){
                lastInserted = values["Items"][i];
            }
        }
        
        
        return { 
            StatusCode: 200, StatusMessage: 'Data Read Successfully','Body':lastInserted
            
        }; 
    }catch(err){
        return {
            StatusCode: 400,
            StatusMessage: "Wrong table provided"
        };
    }
};
