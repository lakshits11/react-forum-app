import React, { Component } from 'react';
import GuestNav from './guestnav';
import UserNav from './usernav';

class UserMenu extends Component {
  render() {
    if (!this.props.isAuthenticated) {
      return (
        <UserNav
          username={this.props.username}
          avatar={this.props.avatar}
        />
      );
    } else {
      return (
        <GuestNav />
      );
    }
  }
}

export default UserMenu;