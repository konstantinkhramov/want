import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import { AppComponent }   from './app.component';

import { HomeComponent } from './home/home.component';
import {AppRoutingModule} from "./app-routing.module";
import {APP_BASE_HREF} from "@angular/common";
import {HttpClientModule} from "@angular/common/http";


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
        {provide: APP_BASE_HREF, useValue : '/' }
    ],
    bootstrap: [
        AppComponent
    ]
})
export class AppModule { }