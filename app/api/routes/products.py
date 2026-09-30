from fastapi import APIRouter, HTTPException

from app.core.supabase import supabase



router = APIRouter(

    prefix="/products",

    tags=["Products"]

)





# ============================================================
# GET ALL PRODUCTS
# ============================================================


@router.get("")
def get_products():


    try:


        response = (

            supabase

            .table("products")

            .select(
                """
                *,
                product_images(
                    image_url,
                    is_primary
                ),
                product_variants(
                    price,
                    compare_at_price,
                    is_default,
                    is_active
                )
                """
            )

            .eq(
                "status",
                "active"
            )

            .execute()

        )



        products=[]



        for product in response.data:



            # -------------------------
            # IMAGE
            # -------------------------

            image_url=None


            images = product.get(
                "product_images",
                []
            )


            for image in images:


                if image.get(
                    "is_primary"
                ):


                    image_url = image.get(
                        "image_url"
                    )

                    break





            # -------------------------
            # DEFAULT VARIANT PRICE
            # -------------------------

            price=None

            compare_price=None



            variants = product.get(
                "product_variants",
                []
            )



            for variant in variants:


                if (

                    variant.get(
                        "is_default"
                    )

                    and

                    variant.get(
                        "is_active"
                    )

                ):


                    price = variant.get(
                        "price"
                    )


                    compare_price = variant.get(
                        "compare_at_price"
                    )


                    break





            products.append({


                "id":
                product.get("id"),


                "name":
                product.get("name"),


                "slug":
                product.get("slug"),



                "description":
                product.get("description"),



                "short_description":
                product.get(
                    "short_description"
                ),



                "image":
                image_url,



                "price":
                price,



                "compare_at_price":
                compare_price,



                "rating":
                product.get(
                    "average_rating"
                ),



                "review_count":
                product.get(
                    "review_count"
                )


            })



        return products





    except Exception as error:


        raise HTTPException(

            status_code=500,

            detail=str(error)

        )








# ============================================================
# GET CATEGORIES
# ============================================================


@router.get("/categories")
def get_categories():


    try:


        response = (

            supabase

            .table("categories")

            .select("*")

            .execute()

        )


        return response.data



    except Exception as error:


        raise HTTPException(

            status_code=500,

            detail=str(error)

        )







# ============================================================
# GET PRODUCT BY SLUG
# ============================================================


@router.get("/{slug}")
def get_product_by_slug(
    slug:str
):


    try:


        response=(

            supabase

            .table("products")

            .select(
                """
                *,
                product_images(*),
                product_variants(*)
                """
            )

            .eq(
                "slug",
                slug
            )

            .single()

            .execute()

        )


        return response.data



    except Exception as error:


        raise HTTPException(

            status_code=404,

            detail="Product not found"

        )