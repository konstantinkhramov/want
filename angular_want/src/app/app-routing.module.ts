import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {HomeComponent} from "./home/home.component";
import {AuthGuard} from "./_guards";
import {LoginComponent} from "./account/login.component";
import {RegisterComponent} from "./account/register.component";
import {LayoutComponent} from "./account/layout.component";


const accountModule = () => import('./account/account.module').then(x => x.AccountModule);

const routes: Routes = [
    // {path: '', component: HomeComponent, canActivate: [AuthGuard]},
    {path: '', component: HomeComponent, pathMatch: 'full'},
    {path: 'account', loadChildren: accountModule},
        // otherwise redirect to home
    { path: '**', redirectTo: '' }
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule {
}