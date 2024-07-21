// import { useSelector } from 'react-redux';
import { Navigate,Outlet } from 'react-router-dom';
import { useContext } from 'react';
import Authuser from '../context/aut';
export default function Protectedrt(){
    const { user } = useContext(Authuser); 

    
    return  user ? <Outlet /> :<Navigate to="login"/>;

   
}