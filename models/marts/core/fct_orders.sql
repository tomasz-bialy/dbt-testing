with orders as (

    select * from {{ ref('stg_orders') }}

),

payments as (

    select * from {{ ref('stg_payments')}}

)

select
    customer_id,
    orderid,
    amount
from
    payments
inner join
    orders on orders.order_id = payments.orderid