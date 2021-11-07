const AWS = require('aws-sdk');
const dynamo = new AWS.DynamoDB.DocumentClient({region: 'us-east-2'});

exports.handler = async (event, context, callback) => {
    const requestId = context.awsRequestId;

    if(event['Request'] =='insert'){
        let operation = (event['operacion'] =='0001')?'suma':(event['operacion'] =='0010')?'resta':(event['operacion'] =='0100')?'multiplicacion':(event['operacion'] =='1000')?'division':'operacion invalida';
   
        if (operation == 'operacion invalida'){
            return {
            'display': operation
        };
        }
        else {
            
            //call insert method and passing the event recieved parametres
            await insertData(requestId,event,operation).then(() => {
                callback(null, {
                    display: operation + ' guardada exitosamente'
                });
            }).catch((err) => {
                console.error(err);
            });
        }
    }  
    else if(event['Request'] =='update'){
        let result =0;
        let signo = '+';
        switch (event['Operation']) {
            case 'suma':
                result =  parseFloat(event['Count']) + parseFloat(event['InputNumber']);
                break;
            case 'resta':
                result =  parseFloat(event['Count']) - parseFloat(event['InputNumber']);
                signo = '-';
                break;
            case 'multiplicacion':
                result =  parseFloat(event['Count']) * parseFloat(event['InputNumber']);
                signo = '*';
                break;
            case 'division':
                result =  parseFloat(event['Count']) / parseFloat(event['InputNumber']);
                signo = '/';
                break;
            default:
                // code
        }
        await updateData(event, result).then(() => {
                    callback(null, {
                        result: event['Count'] + ' '+ signo + ' ' + event["InputNumber"] + ' = '+ result
                    });
                }).catch((err) => {
                    console.error(err);
                });
    }
 
};
//insert send the data to the dynamoDB table, using and recieving the parametres from the invoker lambda
function insertData(requestId,event,operation) {
    //get the current datetime, replacing unwished chars and adding milliseconds 
    var date  = new Date();
    //set data to insert in db
    var values = {
        'UUID' : requestId,
        'Date': date.toISOString().slice(0, 19).replace("T", " ") + ':'+ (new Date().getMilliseconds()),
        'Count': event['contador'],
        'Device':event['dispositivo'],
        'Operation':operation,
        'TimeStampUpdated': +date,
        'OperationResult':Number( event['contador']).toFixed(2)

    };
     const params = {
        TableName: 'Binnacle',
        Item: values
    };
    //write data in the table
    return dynamo.put(params).promise();
    
}
//update a registre in data base
function updateData(event,result){
    let params =  {
        TableName: 'Binnacle',
            Key: {
                'UUID': event['UUID']
            },
        UpdateExpression: `set OperationResult = :re, InputNumber = :in, TimeStampUpdated = :ts `,
        ExpressionAttributeValues: {
            ":re": result.toFixed(2),
            ":in": event['InputNumber'],
            ":ts": +new Date()
        },
    };
    try{
        return dynamo.update(params).promise();
    }catch(err){
        console.log(err);
    }
}