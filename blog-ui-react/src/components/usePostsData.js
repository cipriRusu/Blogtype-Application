import React, { useEffect, useState } from 'react';

function usePostsData(){
    const[allData, setData] = useState([]);

    useEffect(() => {
        let mounted = true;
        fetch('http://localhost:4449/api/posts/')
            .then(response => response.json())
            .then(data => {
                if (mounted) {
                    setData(data)
                }
            })
        return () => mounted = false;
    }, []
    )
    return allData;
};

export default usePostsData