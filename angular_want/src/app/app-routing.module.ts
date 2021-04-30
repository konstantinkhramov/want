import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {HomeComponent} from "./home/home.component";
import {AuthGuard} from "./_guards";
import {SignupComponent} from "./signup/signup.component";


const accountModule = () => import('./account/account.module').then(x => x.AccountModule);

const routes: Routes = [
    {path: '', component: HomeComponent, pathMatch: 'full', canActivate: [AuthGuard]},
    {path: 'account', loadChildren: accountModule},
    {path: 'signup', component: SignupComponent},
        // otherwise redirect to home
    { path: '**', redirectTo: '' }
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule {
}
