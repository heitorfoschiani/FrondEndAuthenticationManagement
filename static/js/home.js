async function get_user_access_token() {
    const response = await fetch('http://127.0.0.1:5000/get-api-access-token');
    
    if (response.status === 200) {
        const data = await response.json();
        const access_token = data.access_token;

        return access_token;
    };
};

window.onload = async function() {
    const access_token = await get_user_access_token();
    console.log(access_token);
};