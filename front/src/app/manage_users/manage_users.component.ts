import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { UsersService } from '../services/users.service';
import { CheckAuthentication } from '../services/auth.service';

@Component({
  selector: 'app-manage-users',
  templateUrl: './manage_users.component.html',
  styleUrls: ['./manage_users.component.scss']
})
export class ManageUsersComponent implements OnInit {

  ngOnInit() {
    this.load();
  }

  constructor(
    private usersService: UsersService,
    private checkAuthentication: CheckAuthentication,
    private router: Router
  ) { }

  listUsers = [];
  type = 'Add'
  user = {
    id: '',
    name: '',
    age: '',
    sex: '',
    email: ''
  }

  load() {
    this.usersService.getAllUsers().subscribe(response => {
      if (this.checkAuthentication.check(response)) { return; }
      else {
        var result = JSON.parse(response);
        this.listUsers = result.data
      }
    });
  }

  submit() {
    if (this.type == 'Add') {
      this.usersService.addUser(this.user.id, this.user.name, this.user.sex, this.user.age, this.user.email).subscribe(response => {
        if (this.checkAuthentication.check(response)) { return; }
        else {
          var result = JSON.parse(response);
          alert(result.data);
          this.load();
        }
      });
    }
    else {
      this.usersService.updateUser(this.user.id, this.user.name, this.user.sex, this.user.age, this.user.email).subscribe(response => {
        if (this.checkAuthentication.check(response)) { return; }
        else {
          var result = JSON.parse(response);
          alert(result.data);
          this.load();
        }
      });
    }
  }

  create() {
    this.type = 'Add';
    this.user = {
      id: '',
      name: '',
      age: '',
      sex: '',
      email: ''
    }
  }

  update(id) {
    this.type = 'Edit'
    var userEdit = this.listUsers.filter(item => item.id == id)[0];
    this.user.id = userEdit.id;
    this.user.name = userEdit.name;
    this.user.age = userEdit.age;
    this.user.sex = userEdit.sex;
    this.user.email = userEdit.email;

  }

  delete(id) {
    this.usersService.deleteUser(id).subscribe(response => {
      if (this.checkAuthentication.check(response)) { return; }
      else {
        var result = JSON.parse(response);
        alert(result.data);
        this.load();
      }
    });
  }

  logout() {
    this.usersService.logout().subscribe(response => {
      if (this.checkAuthentication.check(response)) { return; }
      else {
        localStorage.removeItem('currentUser');
        this.router.navigate(['/login']);
      }
    });
  }
}
