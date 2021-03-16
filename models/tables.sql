-- 货物信息表
create table if not exists goods (
    id integer primary key autoincrement,
    name varchar(64) not null,
    goods_type tinyint not null,
    create_time datetime not null,
    comment text
);
create unique index if not exists goods_name_type
    on goods(name, goods_type);

-- 成本表
create table if not exists costs (
    id integer primary key autoincrement,
    goods_id integer not null,
    cost_type tinyint not null,
    cost decimal(10, 2) not null default(0),
    foreign key (goods_id) references goods(id)
);

-- 订单表
create table if not exists orders (
    id integer primary key autoincrement,
    order_type tinyint not null,
    customer varchar(64) not null,
    create_time datetime not null,
    comment text
);

-- 订单日志表
create table if not exists order_logs (
    id integer primary key autoincrement,
    order_id integer not null,
    event tinyint not null,
    time datetime not null,
    foreign key (order_id) references orders(id)
);
create index if not exists order_logs_order_id 
    on order_logs(order_id);

-- 订单详情表
create table if not exists order_detail (
    id integer primary key autoincrement,
    order_id integer not null,
    goods_id integer not null,
    item_id integer not null,
    total integer not null default(0),
    price decimal(10, 2) not null,
    create_time datetime not null,
    comment text,
    foreign key (order_id) references orders(id),
    foreign key (goods_id) references goods(id)
);
create index if not exists order_detail_order_id
    on order_detail(order_id);
create index if not exists order_detail_goods_item_id
    on order_detail(goods_id, item_id);

-- jk库存尺码表
create table if not exists jk_inventory (
    id integer primary key autoincrement,
    goods_id integer not null,
    serial_number text not null,
    size_code varchar(10) not null,
    length smallint not null,
    total integer not null,
    foreign key (goods_id) references goods(id)
);
create unique index if not exists jk_serial_number
    on jk_inventory(serial_number);
create index if not exists jk_size_length
    on jk_inventory(goods_id, size_code, length);

-- 小物库存尺码表
create table if not exists accessories_inventory (
    id integer primary key autoincrement,
    type tinyint not null,
    serial_number text not null,
    goods_id integer not null,
    associate_goods integer comment `如果是搭着卖的小物这里可以记录衣服的商品id`,
    total integer not null,
    foreign key (goods_id) references goods(id)
);
create unique index if not exists accessories_serial_number
    on accessories_inventory(serial_number);