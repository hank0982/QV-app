import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { WelcomeComponent } from './welcome/welcome.component';
import { QuestionnaireComponent } from './questionnaire/questionnaire.component';
import { EndPageComponent } from './end-page/end-page.component';


const routes: Routes = [
  { path: '', component: WelcomeComponent },
  { path: 'questionnaire', component: QuestionnaireComponent},
  { path: 'end', component: EndPageComponent}
]

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
