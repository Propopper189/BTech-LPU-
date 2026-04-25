enum Product {
    PEN(10), NOTEBOOK(50), BAG(500);

    int price;

    Product(int price) {
        this.price = price;
    }

    int getPrice() {
        return price;
    }
}

class important2 
{
    public static void main(String[] args) {
        System.out.println(Product.PEN.getPrice());
        System.out.println(Product.BAG.getPrice());
    }
}