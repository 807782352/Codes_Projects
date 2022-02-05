from db_english.mysql_db import pool


class NewsDao:
    # 查询第N页的待审批新闻列表
    def search_unreview_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.id,n.title,t.type,u.username " \
                  "FROM t_news n JOIN t_type t ON n.type_id=t.id " \
                  "JOIN t_user u ON u.id=n.editor_id " \
                  "WHERE n.state=%s " \
                  "ORDER BY n.create_time DESC " \
                  "LIMIT %s,%s "
            cursor.execute(sql, ("Pending", (page - 1) * 10, 10))  # 假设一页十条记录
            result = cursor.fetchall()
            return result

        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查询待审批新闻的总页数
    def search_unreview_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT CEIL(COUNT(*)/10) FROM t_news " \
                  "WHERE state=%s"
            cursor.execute(sql, ["Pending"])  # 假设一页十条记录
            count_page = cursor.fetchone()[0]
            return count_page

        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 审批新闻
    def update_unreview_news(self,id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "UPDATE t_news SET state=%s WHERE id=%s "
            cursor.execute(sql, ("Approved",id))  # 假设一页十条记录
            con.commit()
            # count_page = cursor.fetchone()[0]   不需要这行了 因为你现在是要写在SQL数据库里，而不是打印出来

        except Exception as e:
            if "con" in dir():
                con.rollback()
        finally:
            if "con" in dir():
                con.close()



    # 查询第N页的所有新闻列表
    def search_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.id,n.title,t.type,u.username " \
                  "FROM t_news n JOIN t_type t ON n.type_id=t.id " \
                  "JOIN t_user u ON u.id=n.editor_id " \
                  "ORDER BY n.create_time DESC " \
                  "LIMIT %s,%s "
            cursor.execute(sql, ((page - 1) * 10, 10))  # 假设一页十条记录
            result = cursor.fetchall()
            return result

        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查询所有新闻的总页数
    def search_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT CEIL(COUNT(*)/10) FROM t_news "
            cursor.execute(sql)  # 假设一页十条记录
            count_page = cursor.fetchone()[0]
            return count_page

        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 删除新闻
    def delete_by_id(self,id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "DELETE FROM t_news WHERE id=%s "
            cursor.execute(sql, [id])  # 假设一页十条记录
            con.commit()
            # count_page = cursor.fetchone()[0]   不需要这行了 因为你现在是要写在SQL数据库里，而不是打印出来

        except Exception as e:
            if "con" in dir():
                con.rollback()
        finally:
            if "con" in dir():
                con.close()

#测试代码
# service=NewsDao()
# result = service.search_unreview_list(1)
# print(result)
