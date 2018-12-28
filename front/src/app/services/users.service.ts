import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UsersService {

  constructor(
    private http: HttpClient
  ) { }

  getAllUsers() {
    return this.http.get<any>('api/all_users');
  }

  deleteUser(id) {
    var params = {id: id}
    return this.http.post<any>('api/delete_user', params);
  }

  addUser(id, name, sex, age, email) {
    var params = {
      id: id,
      name: name,
      sex: sex,
      age: age,
      email: email
    }
    return this.http.post<any>('api/add_user', params);
  }

  updateUser(id, name, sex, age, email) {
    var params = {
      id: id,
      name: name,
      sex: sex,
      age: age,
      email: email
    }
    return this.http.post<any>('api/update_user', params);
  }
}
