##  掲示板サイト

このサイトは**バスケ**についての議題を掲示板に書き込み会話していくサイトです

## ER図

```mermaid
erDiagram
    user {
        int id pk
        char name
        char mailaddress
        char passward
    }

    

    posts{
        int post_id pk
        int user_id fk
        date created_at
    }

    comment{
        int comment_id pk
        int user_id fk
        int post_id fk
        date created_at
    }

    user ||--o{ posts : ""
    user ||--o{ comment : ""
    posts ||--o{ comment : ""

```