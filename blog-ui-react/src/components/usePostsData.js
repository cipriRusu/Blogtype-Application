import React, { useEffect, useState } from 'react';

function usePostsData(currentRoute){
    const[allData, setData] = useState([]);
    console.log(currentRoute)

    useEffect(() => {
        let mounted = true;
        fetch(currentRoute)
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