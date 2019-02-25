import { Injectable } from '@angular/core';
import { Router, CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {
    constructor(private router: Router) { }
    canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
        if (localStorage.getItem('currentUser')) {
            return true;
        }
        this.router.navigate(['/login']);
        return false;
    }
}

@Injectable({
  providedIn: 'root'
})
export class LoggedIn implements CanActivate {
    constructor(private router: Router) { }
    canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
        if (localStorage.getItem('currentUser')) {
            this.router.navigate(['/users']);
            return false;
        }
        return true;
    }
}

@Injectable({
  providedIn: 'root'
})
export class CheckAuthentication {
    constructor(private router: Router) { }
    check(response) {
        var data = JSON.parse(response.replace(/NaN/g, 'null'));
        if (data.code == 601) {
            localStorage.removeItem('currentUser')
            this.router.navigate(['/login']);
            return true;
        }
        return false;
    }
}
