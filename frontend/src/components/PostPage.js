import React, { useState } from 'react';
import Header from './Header';
import HeaderSmall from './HeaderSmall';
import { Link } from 'react-router-dom';
import '../style/post.css';
import ImageList from './ImageList';
import ThumbUpIcon from "@mui/icons-material/ThumbUp";
import ThumbDownIcon from "@mui/icons-material/ThumbDown";

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
                    <div className='title'><h2>Zaba biega</h2></div>
                    <div className='photos'>
                        <img src={require('../images/testowe/2.gif')}/>
                    </div>
                
                <div className='description'><div className='username'>GigaChad69: 30.05.2023 16:50</div>Fajowa zaba biegnie a potem jeszcze biegnie a na koniec</div>
                <div className='opinions'>
                    <div className='likes'><div className='likeImg'><ThumbUpIcon sx={{fontSize:15}}/></div>1566666</div>
                    <div className='dislikes'><div className='dislikeImg'><ThumbDownIcon sx={{fontSize:15}}/></div>2312</div>
                </div>

                <div className='commentsSection'><div className='commentTitle'>Komentarze</div>
                        <div className='comment1'><div className='username'>Grażynka13: 30.05.2023 17:00</div><div className='com'>Fajowe zdjecie tak sie smialam ze zafajdalam majtasy</div></div>
                        <div className='comment1'><div className='username'>Wojtuś09: 30.05.2023 17:00</div><div className='com'> ciekawe gdzie tak biegnie</div></div>
                        <div className='addComment'><div className='addcommentTitle'>Dodaj komentarz</div>
                            <div><textarea name="Text" cols="50" rows="3" style={{ border: '1.5px solid #f7971d'}}></textarea></div>
                            <button type='submit' className='commentSubmit'>Dodaj</button>
                    </div>
                    </div>
                </div>
                </div>
                

            </div>
    )
}
export default PostPage


