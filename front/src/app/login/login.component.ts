import { Component, OnInit } from '@angular/core';
import { UsersService } from '../services/users.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  returnUrl = '';

  ngOnInit() {
  }

  constructor(
    private usersService: UsersService,
    private router: Router,

  ) { }

  user_mail = '';
  password = '';


  login() {
    this.usersService.login(this.user_mail, this.password).subscribe(response => {
      var result = JSON.parse(response);
      if (result.code == 200) {
        localStorage.setItem('currentUser', JSON.stringify({email: this.user_mail}));
        this.router.navigate(['/users']);
      }
      else {
        alert('Email or password wrong!!!');
      }
    });
  }
}
