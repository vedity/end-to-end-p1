import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { User } from '../models/auth.models';

@Injectable({ providedIn: 'root' })
export class AuthfakeauthenticationService {
    private currentUserSubject: BehaviorSubject<User>;
    public currentUser: Observable<User>;
    baseUrl = 'http://127.0.0.1:8000/mlaas/'
    headers = new HttpHeaders ({
      'Content-type': 'application/json',
    });
    
    constructor(private http: HttpClient) {
        this.currentUserSubject = new BehaviorSubject<User>(JSON.parse(localStorage.getItem('currentUser')));
        this.currentUser = this.currentUserSubject.asObservable();
    }

    public get currentUserValue(): User {
        return this.currentUserSubject.value;
    }

    login(email: string, password: string) {
        var params=new HttpParams().append("user_name",email).append("password",password);
        return this.http.get<any>(this.baseUrl+`common/user/login/`,{headers:this.headers,params})
            .pipe(map(user => {
                // login successful if there's a jwt token in the response
                if (user) {
                    var userdata=new User();
                    userdata.email=email;
                    userdata.firstName=email;
                    userdata.id=1;
                    userdata.username=email;
                    // store user details and jwt token in local storage to keep user logged in between page refreshes
                    localStorage.setItem('currentUser', JSON.stringify(userdata));
                    this.currentUserSubject.next(userdata);
                }
                return user;
            }));
    }
    // login(email: string, password: string) {
    //     return this.http.post<any>(`/users/authenticate`, { email, password })
    //         .pipe(map(user => {
    //             // login successful if there's a jwt token in the response
    //             if (user && user.token) {
    //                 // store user details and jwt token in local storage to keep user logged in between page refreshes
    //                 localStorage.setItem('currentUser', JSON.stringify(user));
    //                 this.currentUserSubject.next(user);
    //             }
    //             return user;
    //         }));
    // }

    logout() {
        // remove user from local storage to log user out
        localStorage.removeItem('currentUser');
        this.currentUserSubject.next(null);
    }
}
