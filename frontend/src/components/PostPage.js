import React, { useState } from 'react';
import Header from './Header';
import HeaderSmall from './HeaderSmall';
import { Link } from 'react-router-dom';
import '../style/post.css';
import ImageList from './ImageList';

import Tag from './Tag';


const PostPage = () => {


    return(

        <div className='homepage'>
            <div className='header'>
                <div className='navBar'>
                        <div className='logoSmall'>
                            <HeaderSmall/>
                        </div>
                        
                        <div className='searchLine'>
                            <form><input className='search' type='text' ></input></form>
                            <div className='searchButton'>
                                <button type="submit" className='searchForm'>Search</button>
                            </div>
                        </div>
                        <div className='buttomsNav'>
                            <div className='registrationButton'>

                                <Link to="/Register" className='signUp'>Sign up</Link>
                            </div>

                            <div className='loginButton'>
                                <Link to="/Login" className="signIn">Sign in</Link>
                            </div>
                        </div>

                    </div>

                    <div className='categoryBar'>
                        <Tag/>
                        

                    </div>
                </div>
                <div className='content'>
                    <div className='photoSection'>
                    <div className='title'>Zaba bieg\</div>
                    <div className='photos'>
                        <img src={require('../images/testowe/2.gif')}/>
                    </div>
                
                <div className='description'>Fajowe zdjecie tak sie smialem ze zafajdalem majtasy</div>
                <div className='opinions'>
                    <div className='likes'>1566666</div>
                    <div className='dislikes'>2312</div>
                </div>

                
                <div className='comment1'><div className='username'>Username: 30.05.2023 17:00</div><div className='com'>fajowa zabafajowa zabafajowa zabafajowa zabafajowa zabafajowa zaba</div></div>
                <div className='comment1'><div className='username'>Username: 30.05.2023 17:00</div><div className='com'> ciekawe gdzie tak biegnie</div></div>
                </div>
                </div>
                

            </div>
    )
}
export default PostPage


