// 监听搜索框的回车事件
document.getElementById('search-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        performSearch();
    }
});

// 执行搜索
function performSearch() {
    const searchInput = document.getElementById('search-input');
    const searchTerm = encodeURIComponent(searchInput.value.trim());
    
    if (searchTerm) {
        // 重定向到 Google 搜索结果页面
        window.location.href = `https://www.google.com/search?q=${searchTerm}`;
    }
}

// 为"手气不错"按钮添加点击事件
document.querySelector('.search-buttons button:last-child').addEventListener('click', function() {
    const searchInput = document.getElementById('search-input');
    const searchTerm = encodeURIComponent(searchInput.value.trim());
    
    if (searchTerm) {
        // 重定向到 Google "手气不错"搜索
        window.location.href = `https://www.google.com/search?q=${searchTerm}&btnI`;
    }
}); 