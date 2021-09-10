import React from 'react';
import Login from './AppPages/Login';
import ViewLoaders from './AppPages/ViewLoaders';
// import NavBar from './components/NavBar'
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";
function App() {
  return (
    <Router >
      <div>
        {/* <NavBar /> */}
        <Switch>
          <Route path="/" exact>
            <Login />
          </Route>
          <Route path="/viewLoaders">
            <ViewLoaders />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
