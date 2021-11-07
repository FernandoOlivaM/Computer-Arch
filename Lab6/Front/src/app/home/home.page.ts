import { Component, Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
@Injectable()

export class HomePage {

  constructor(public http: HttpClient) {}
  tableHeaders = ["UUID", "Date", "Device", "Count", "Operation"]; 
  tableContent=[]
  showAlert: boolean = false;   Alert_Text = "";  Alert_Status = "";  Alert_Color = "";


  async ngOnInit() {
    let count =0;
    while(true){
      count++;
      var data = await this.GetData()
      console.log(data)
      let element = data['Body'];
  
        let transactionHistory = [];
        for(let j = 0; j < this.tableHeaders.length; j++){
          transactionHistory.push({
            [`${this.tableHeaders[j]}`]: element[`${this.tableHeaders[j]}`]
          })
          
        }
        this.tableContent.push(transactionHistory);
        
      
      console.log(this.tableContent)
      await this.sleep(20000);
      this.tableContent=[]

      console.log(count)

    }
    
  }
  async sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  
  async GetData(){
    var Api_URL = "https://xqgua01dfk.execute-api.us-east-2.amazonaws.com/GetData/getdata"
    return new Promise(
      resolve => {
      this.http.get(Api_URL)
      .subscribe(
        data =>  resolve(data),
        err => {
          console.log(err); 
          resolve(err);
        })
    });
  }
  async send(InputNumber){
    let urlRequest = "https://i7dc18qycl.execute-api.us-east-2.amazonaws.com/Connection/connection";
    let result;
    this.showAlert = false;
    try {
      await fetch(urlRequest, {
        method: 'POST',
        body: JSON.stringify({
          "UUID": this.tableContent[0][0]['UUID'],
          "Request": "update",
          "Count": this.tableContent[0][3]['Count'],
          "Operation": this.tableContent[0][4]['Operation'],
          "InputNumber": parseFloat(InputNumber.value)
        })
      })
        .then((data) => data.json())
        .then((value) => (result = value));
    } catch (err) {
      console.error(err);
    }
    console.log(result)
    this.Alert_Text="La operación se ha realizado con exito. \n"+ result['result'];
    this.Alert_Status="Success ! ";
    this.Alert_Color="alertSuccess";//green color
    this.showAlert = true;

    return result['result'];
  }

}
