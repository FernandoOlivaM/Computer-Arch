const AWS = require('aws-sdk');
const dynamo = new AWS.DynamoDB.DocumentClient({region: 'us-east-2'});

exports.handler = async (event, context, callback) => {
    let output = '';
    const requestId = context.awsRequestId;
  
    switch (event['contador']) {
        case 10:
            output='11111011';
        break;
        case 9:
            output='01100000';
        break;
        case 8:
            output='11011100';
        break;
        case 7:
            output='11110100';
        break;
        case 6:
            output='01100111';
        break;
        case 5:
            output='10110110';
        break;
        case 4:
            output='10111111';
        break;
        case 3:
            output='11100001';
        break;
        case 2:
            output='11111111';
        break;
        case 1:
            output='11110110';
        break;
        default:
            console.log('out of range');
    }
   
  
    //call writeMessage method and passing the event recieved parametres
    await writeMessage(requestId,event).then(() => {
        callback(null, {
            display: output
        });
    }).catch((err) => {
        console.error(err);
    });
     return {
        'display': output
    };
    
 
};
//writeMessage send the data to the dynamoDB table, using and recieving the parametres from the invoker lambda
function writeMessage(requestId,event) {
    //get the current datetime, replacing unwished chars and adding milliseconds 
    var date  = (new Date()).toISOString().slice(0, 19).replace("T", " ") + ':'+ (new Date().getMilliseconds());
    //set data to insert in db
    var values = {
        'UUID' : requestId,
        'Date': date,
        'Count': event['contador'],
        'Device':event['dispositivo']

    };
     const params = {
        TableName: 'Binnacle',
        Item: values
    };
    //write data in the table
    return dynamo.put(params).promise();
    
}