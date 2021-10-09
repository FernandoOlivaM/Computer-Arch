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
  tableHeaders = ["Date", "Message","Status"]; 
  tableContent=[]


  async ngOnInit() {
    var data = await this.GetData()
    console.log(data)
    data['Body'].forEach(element => {

      let transactionHistory = [];
      for(let j = 0; j < this.tableHeaders.length; j++){
        transactionHistory.push({
          [`${this.tableHeaders[j]}`]: element[`${this.tableHeaders[j]}`]
        })
        
      }
      this.tableContent.push(transactionHistory);
      
    });
    console.log(this.tableContent)
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

}
