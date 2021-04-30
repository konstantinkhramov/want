import {NgModule} from "@angular/core";
import {BrowserModule} from "@angular/platform-browser";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {HttpClientModule} from "@angular/common/http";
import {AppRoutingModule} from "./app-routing.module";
import {AppComponent} from "./app.component";
import {HomeComponent} from "./home/home.component";
import {APP_BASE_HREF} from "@angular/common";
import {SignupComponent} from "./signup/signup.component";
import {NgbModule} from "@ng-bootstrap/ng-bootstrap";
import {FooterComponent} from "./shared/footer/footer.component";
import {NavbarComponent} from "./shared/navbar/navbar.component";


@NgModule({
    imports: [
        BrowserModule,
        FormsModule,
        ReactiveFormsModule,
        HttpClientModule,
        AppRoutingModule,
        NgbModule
    ],
    declarations: [
        AppComponent,
        FooterComponent,
        NavbarComponent,
        HomeComponent,
        SignupComponent
    ],
    providers: [
        {provide: APP_BASE_HREF, useValue: window['_app_base'] || '/' }
    ],
    bootstrap: [
        AppComponent
    ]
})
export class AppModule { }
