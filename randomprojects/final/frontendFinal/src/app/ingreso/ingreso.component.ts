import { Component, OnInit } from '@angular/core';
import { HttpClient} from '@angular/common/http';
@Component({
  selector: 'app-ingreso',
  templateUrl: './ingreso.component.html',
  styleUrls: ['./ingreso.component.css']
})
export class IngresoComponent implements OnInit {

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.setBackgroundColor();

  };
  onSave(): any{
    var red = <HTMLInputElement>document.getElementById("red");
    var green = <HTMLInputElement>document.getElementById("green");
    var blue = <HTMLInputElement>document.getElementById("blue");
    var color = <HTMLInputElement>document.getElementById("nombrecolor");
    var post_json = {
      "nombre": color.value,
      "rojo": red.value,
      "verde": green.value,
      "azul": blue.value

    };
    console.log(post_json)
    this.http.post<any>('http://localhost:3000/color', post_json).subscribe({
        next: data => {
          alert("Agregado correctamente");
            var n = <HTMLInputElement>document.getElementById("nombrecolor");
            n.value = "";
        },
        error: error => {
            console.error('There was an error!', error);
        }
    })


  };
   rgbToHex (rgb: any): any {
    var hex = Number(rgb).toString(16);
    if (hex.length < 2) {
         hex = "0" + hex;
    }
    return hex;
  };
  fullColorHex(r : any,g: any,b:any): any {
    var red = this.rgbToHex(r);
    var green = this.rgbToHex(g);
    var blue = this.rgbToHex(b);
    return red+green+blue;
  };
  setBackgroundColor():any{
    var red = <HTMLInputElement>document.getElementById("red");
    var green = <HTMLInputElement>document.getElementById("green");
    var blue = <HTMLInputElement>document.getElementById("blue");
    var hex = this.fullColorHex(red.value, green.value, blue.value)
    var div = <HTMLDivElement>document.getElementById("colorpicker");
    div.style.backgroundColor = "#"+hex;


  }

}
