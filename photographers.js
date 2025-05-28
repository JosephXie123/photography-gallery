// 摄影师数据
const photographers = {
    'fan_ho': {
        name: '何藩',
        bio: '何藩（1931-2016）是香港最著名的摄影师之一，以其独特的黑白街头摄影作品闻名于世。他的作品体现了20世纪50-60年代香港的市井生活，充满诗意和人文关怀。',
        category: '街头摄影',
        image: 'images/photographers/fan_ho.jpg',
        works: [
            {
                title: '午后即景',
                description: '1959年，香港中环',
                image: 'images/works/fan_ho_1.jpg'
            },
            {
                title: '梯级',
                description: '1961年，香港',
                image: 'images/works/fan_ho_2.jpg'
            },
            {
                title: '背影',
                description: '1963年，香港',
                image: 'images/works/fan_ho_3.jpg'
            }
        ]
    },
    'wang_fuchun': {
        name: '王福春',
        bio: '王福春（1943-）是中国著名纪实摄影家，以其《中国火车》系列作品闻名。他用镜头记录了30多年来中国铁路上的人文故事，展现了中国社会的变迁。',
        category: '纪实摄影',
        image: 'images/photographers/wang_fuchun.jpg',
        works: [
            {
                title: '春运',
                description: '1995年，北京站',
                image: 'images/works/wang_1.jpg'
            },
            {
                title: '列车上的生活',
                description: '2001年，青藏线',
                image: 'images/works/wang_2.jpg'
            },
            {
                title: '候车室',
                description: '1998年，哈尔滨站',
                image: 'images/works/wang_3.jpg'
            }
        ]
    },
    'zhang_jc': {
        name: '张家诚',
        bio: '张家诚是一位著名的时尚摄影师，以其独特的视角和创新的拍摄手法在时尚摄影领域享有盛誉。他的作品经常出现在各大时尚杂志中，展现了独特的东方美学。',
        category: '时尚摄影',
        image: 'images/photographers/zhang_jc.jpg',
        works: [
            {
                title: '东方韵',
                description: '2020年，上海时装周',
                image: 'images/works/zhang_1.jpg'
            },
            {
                title: '现代旗袍',
                description: '2021年，北京',
                image: 'images/works/zhang_2.jpg'
            },
            {
                title: '都市映像',
                description: '2022年，广州',
                image: 'images/works/zhang_3.jpg'
            }
        ]
    },
    'zeng_wu': {
        name: '曾无',
        bio: '曾无是新生代时尚摄影师的代表人物，擅长将传统元素与现代时尚完美融合。他的作品充满实验性和创新精神，为中国时尚摄影带来了新的可能性。',
        category: '时尚摄影',
        image: 'images/photographers/zeng_wu.jpg',
        works: [
            {
                title: '新中式',
                description: '2023年，成都',
                image: 'images/works/zeng_1.jpg'
            },
            {
                title: '光影交错',
                description: '2022年，深圳',
                image: 'images/works/zeng_2.jpg'
            },
            {
                title: '未来主义',
                description: '2023年，杭州',
                image: 'images/works/zeng_3.jpg'
            }
        ]
    }
    // 可以继续添加更多摄影师数据
};

// 页面加载时检查是否在详情页
document.addEventListener('DOMContentLoaded', function() {
    const urlParams = new URLSearchParams(window.location.search);
    const photographerId = urlParams.get('id');
    
    if (photographerId && photographers[photographerId]) {
        loadPhotographerDetails(photographerId);
    }
});

// 加载摄影师详情
function loadPhotographerDetails(id) {
    const photographer = photographers[id];
    if (!photographer) return;

    // 更新页面标题
    document.title = `${photographer.name} - 摄影作品集`;

    // 更新个人信息
    document.getElementById('photographerImage').src = photographer.image;
    document.getElementById('photographerName').textContent = photographer.name;
    document.getElementById('photographerBio').textContent = photographer.bio;
    document.getElementById('photographerCategory').textContent = photographer.category;

    // 加载作品集
    const worksGrid = document.getElementById('worksGrid');
    worksGrid.innerHTML = '';

    photographer.works.forEach(work => {
        const workElement = document.createElement('div');
        workElement.className = 'work-item';
        workElement.innerHTML = `
            <img src="${work.image}" alt="${work.title}" 
                 onclick="openLightbox('${work.image}', '${work.title}', '${work.description}')">
        `;
        worksGrid.appendChild(workElement);
    });
}

// Lightbox 功能
function openLightbox(image, title, description) {
    const lightbox = document.getElementById('lightbox');
    const lightboxImage = document.getElementById('lightboxImage');
    const workTitle = document.getElementById('workTitle');
    const workDescription = document.getElementById('workDescription');

    lightboxImage.src = image;
    workTitle.textContent = title;
    workDescription.textContent = description;
    lightbox.classList.add('active');
}

// 关闭 Lightbox
document.querySelector('.close-button').addEventListener('click', function() {
    document.getElementById('lightbox').classList.remove('active');
});

// 点击 Lightbox 背景关闭
document.getElementById('lightbox').addEventListener('click', function(e) {
    if (e.target === this) {
        this.classList.remove('active');
    }
}); 