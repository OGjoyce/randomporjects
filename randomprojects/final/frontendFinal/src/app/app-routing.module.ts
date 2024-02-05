import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ConsultaComponent } from './consulta/consulta.component';
import { IngresoComponent } from './ingreso/ingreso.component';

const routes: Routes = [
  {path: 'consulta', component: ConsultaComponent},
  {path: 'ingreso', component: IngresoComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
