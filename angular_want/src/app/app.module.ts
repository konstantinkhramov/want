import {NgModule} from "@angular/core";
import {BrowserModule} from "@angular/platform-browser";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {HttpClientModule} from "@angular/common/http";
import {AppRoutingModule} from "./app-routing.module";
import {AppComponent} from "./app.component";
import {HomeComponent} from "./home/home.component";
import {APP_BASE_HREF} from "@angular/common";


@NgModule({
    imports: [
        BrowserModule,
        FormsModule,
        ReactiveFormsModule,
        HttpClientModule,
        AppRoutingModule,
    ],
    declarations: [
        AppComponent,
        HomeComponent,
    ],
    providers: [
        {provide: APP_BASE_HREF, useValue: window['_app_base'] || '/' }
    ],
    bootstrap: [
        AppComponent
    ]
})
export class AppModule { }