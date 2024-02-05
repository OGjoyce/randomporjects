import { Component, OnInit } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { HttpClient} from '@angular/common/http';
@Component({
  selector: 'app-consulta',
  templateUrl: './consulta.component.html',
  styleUrls: ['./consulta.component.css']
})
export class ConsultaComponent implements OnInit {
  totalAngularPackages : any;
  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.http.get<any>('http://localhost:3000/color').subscribe(data => {
        this.totalAngularPackages = data.total;
        var html = "";
        for(var i = 0; i<data.colores.length; i++){
          html = html +"<tr>";
          html = html + "<td style='border: 1px solid black'>" + data.colores[i].id + "</td>";
          html = html + "<td style='border: 1px solid black'>" + data.colores[i].nombre + "</td>";
          var color = fullColorHex(data.colores[i].rojo, data.colores[i].verde, data.colores[i].azul)
          html = html + "<td style='background-color: #"+color+"'>" + "</td>";
          html = html + "<td style='border: 1px solid black'  >" + color + "</td>";



        }
        var table = <HTMLTableElement>document.getElementById("tablecolor");
        table.innerHTML = html;


    })
    var rgbToHex = function (rgb: any) {
      var hex = Number(rgb).toString(16);
      if (hex.length < 2) {
           hex = "0" + hex;
      }
      return hex;
    };
    var fullColorHex = function(r : any,g: any,b:any) {
      var red = rgbToHex(r);
      var green = rgbToHex(g);
      var blue = rgbToHex(b);
      return red+green+blue;
    };
  }





}
