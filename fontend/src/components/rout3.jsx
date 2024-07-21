// components/Privaterout.js
import {useContext} from 'react';

import { Outlet, Navigate } from "react-router-dom";
import  { Authpr } from '../context/aut';
// { Authpr } from '../context/aut';
// import PropTypes from "prop-types";

// const Privaterout = ({element: Component, ...rest }) => {
//     const isAuthenticated = false; // Replace this with your actual authentication check

//     return (
//         <Routes>

//         <Route {...rest}>
//             {!isAuthenticated ? (
//                 <Navigate to="login" />
//             ) : (
//                 <Component />
//             )}
//         </Route>
//         </Routes>

//     );
// }

// Privaterout.propTypes={
//     element: PropTypes.node.isRequired
// };
const Snakelane=()=>{
    // let isAuht = true;
    let { condata }= useContext(Authpr);
    console.log(condata,3243234234234)
    let { user }=condata;
    console.log(user)
    const isAut = user !== null;
    console.log("work of private rourrrrrrrrrrrrrrrrrrrrrrrrrrrrrting");
    // console.log(user)
    return(
        isAut ? <Outlet/>:<Navigate to="/"/>
        // user?<Outlet>:<Navigate to ="/"/>
    )
}
export default Snakelane;
